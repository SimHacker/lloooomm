# Empathic SQL Imports for Shneiderman's Owls 🦉🐭

## Current Population Recreation

### Recreate Current Owls (50 owls with current parameters)
```sql
-- Generate current owl population with WIZZIDs and three-color gradients
CREATE TEMPORARY TABLE owl_colors AS 
SELECT * FROM (VALUES
  ('#8B4513', '#D2691E', '#F4A460'), -- Browns
  ('#4B0082', '#8A2BE2', '#9400D3'), -- Purples  
  ('#191970', '#4169E1', '#6495ED'), -- Blues
  ('#8B0000', '#DC143C', '#FF6347'), -- Reds
  ('#556B2F', '#8FBC8F', '#90EE90')  -- Greens
) AS t(inner_color, middle_color, outer_color);

INSERT INTO owls (wizzy_id, inner_color, middle_color, outer_color, 
                  middle_color_pos, timezone, energy, status)
SELECT 
  -- Generate WIZZID with UNIQUE ids (example of ACTIVE COMMENT magic!)
  CHR(65 + (row_num % 26)) || 
  (ARRAY['🦉', '🌳', '🌲', '🍃', '🌙', '⭐', '🌟', '🌌', '🦅', '🪶'])[1 +   (ARRAY['🍂', '🌺', '🌸', '🦜', '🕊️', '🦚', '🦢', '🪺', '🌾', '🌿'])[1 + ((row_num * 3 + 5) % 10)] ||
  CHR(65 + ((row_num * 7 + 13) % 26)) AS wizzy_id,
  
  -- Random colors from our palette
  c.inner_color,
  c.middle_color, 
  c.outer_color,
  
  -- Middle color position varies 20-60%
  0.2 + (random() * 0.4) AS middle_color_pos,
  
  -- Random timezone
  'UTC' || CASE WHEN random() < 0.5 THEN '+' ELSE '-' END || 
  FLOOR(random() * 12)::text AS timezone,
  
  -- Full energy to start
  100 AS energy,
  
  -- Initial status
  'flying' AS status
  
FROM generate_series(1, 50) AS row_num
CROSS JOIN LATERAL (
  SELECT * FROM owl_colors 
  ORDER BY random() 
  LIMIT 1
) c;
```

### Recreate Current Mice (200 mice with current parameters)
```sql
-- Generate current mouse population with WIZZIDs
CREATE TEMPORARY TABLE mouse_colors AS
SELECT * FROM (VALUES  
  ('#D3D3D3', '#A9A9A9', '#696969'), -- Grays
  ('#F5DEB3', '#DEB887', '#D2691E'), -- Tans
  ('#FFD700', '#FFA500', '#FF8C00'), -- Golds
  ('#8B4513', '#A0522D', '#D2691E'), -- Browns
  ('#BC8F8F', '#F4A460', '#FFDEAD')  -- Sandy
) AS t(inner_color, middle_color, outer_color);

INSERT INTO mice (wizzy_id, inner_color, middle_color, outer_color,
                  middle_color_pos, weight, status)
SELECT
  -- Generate WIZZID with UNIQUE ids (example of ACTIVE COMMENT magic!)
  CHR(65 + (row_num % 26)) ||
  (ARRAY['🐭', '🧀', '🌾', '🌽', '🥜', '🍞', '🥖', '🍪', '🪨', '🌰'])[1 +   (ARRAY['🍄', '🥕', '🫘', '🌻', '🌼', '🍀', '🌱', '🪵', '🍃', '🫧'])[1 + ((row_num * 3 + 5) % 10)] ||
  CHR(65 + ((row_num * 7 + 13) % 26)) AS wizzy_id,
  
  -- Random colors
  c.inner_color,
  c.middle_color,
  c.outer_color,
  
  -- Middle color position
  0.2 + (random() * 0.4) AS middle_color_pos,
  
  -- Weight 20-40 grams
  20 + (random() * 20) AS weight,
  
  -- Initial status
  'foraging' AS status
  
FROM generate_series(1, 200) AS row_num  
CROSS JOIN LATERAL (
  SELECT * FROM mouse_colors
  ORDER BY random()
  LIMIT 1
) c;
```

## Enhanced Variations

### Personality-Based Owls
```sql
-- Owls with distinct personalities affecting behavior
INSERT INTO owls (wizzy_id, inner_color, middle_color, outer_color,
                  personality_traits, timezone, energy)
SELECT
  -- WIZZID generation
  CHR(65 + (n % 26)) ||
  emoji1 || emoji2 ||
  CHR(65 + ((n * 7 + 13) % 26)) AS wizzy_id,
  
  -- Personality-influenced colors
  CASE 
    WHEN personality_type = 'aggressive' THEN '#8B0000' -- Dark red
    WHEN personality_type = 'wise' THEN '#4B0082'      -- Indigo
    WHEN personality_type = 'playful' THEN '#FF69B4'   -- Hot pink
    ELSE '#8B4513'                                     -- Brown
  END AS inner_color,
  
  CASE
    WHEN personality_type = 'aggressive' THEN '#DC143C' -- Crimson
    WHEN personality_type = 'wise' THEN '#8A2BE2'      -- Blue violet
    WHEN personality_type = 'playful' THEN '#FFB6C1'   -- Light pink  
    ELSE '#D2691E'                                     -- Chocolate
  END AS middle_color,
  
  CASE
    WHEN personality_type = 'aggressive' THEN '#FF6347' -- Tomato
    WHEN personality_type = 'wise' THEN '#9400D3'      -- Violet
    WHEN personality_type = 'playful' THEN '#FFC0CB'   -- Pink
    ELSE '#F4A460'                                     -- Sandy brown
  END AS outer_color,
  
  -- Personality traits as JSONB
  jsonb_build_object(
    'type', personality_type,
    'hunt_skill', hunt_skill,
    'patience', patience,
    'sociability', sociability,
    'curiosity', curiosity
  ) AS personality_traits,
  
  -- Timezone preferences based on personality
  CASE
    WHEN personality_type = 'wise' THEN 'UTC+0'  -- Wise owls like GMT
    ELSE 'UTC' || (CASE WHEN random() < 0.5 THEN '+' ELSE '-' END) || 
         FLOOR(random() * 12)::text
  END AS timezone,
  
  -- Starting energy based on personality
  CASE
    WHEN personality_type = 'aggressive' THEN 80 + random() * 20
    WHEN personality_type = 'playful' THEN 90 + random() * 10
    ELSE 70 + random() * 30
  END AS energy

FROM (
  SELECT 
    n,
    -- Pick personality type
    (ARRAY['aggressive', 'wise', 'playful', 'cautious'])[1 + FLOOR(random() * 4)::int] AS personality_type,
    -- Emoji selection based on personality tendencies
    CASE 
      WHEN random() < 0.3 THEN '🦉'
      WHEN random() < 0.6 THEN '🦅'
      ELSE (ARRAY['🌳', '🌲', '🍃', '🌙', '⭐', '🌟', '🌌', '🪶'])[1 + FLOOR(random() * 8)::int]
    END AS emoji1,
    (ARRAY['🍂', '🌺', '🌸', '🦜', '🕊️', '🦚', '🦢', '🪺', '🌾', '🌿'])[1 + FLOOR(random() * 10)::int] AS emoji2,
    -- Personality stats
    50 + random() * 50 AS hunt_skill,
    20 + random() * 80 AS patience,
    10 + random() * 90 AS sociability,
    30 + random() * 70 AS curiosity
  FROM generate_series(1, 30) n
) AS personality_data;
```

### Ecosystem Diversity
```sql
-- Multiple species in one ecosystem
INSERT INTO creatures (species, wizzy_id, colors, behavior_params)
VALUES
  -- Night Owls (excellent night vision)
  ('owl', 'N🦉🌙T', 
   ROW('#191970', '#4169E1', '#87CEEB'),
   '{"vision_range": 300, "night_bonus": 2.0, "preferred_altitude": 150}'::jsonb),
   
  -- Forest Owls (camouflaged)
  ('owl', 'F🌲🍃R',
   ROW('#228B22', '#32CD32', '#90EE90'),
   '{"stealth": 0.8, "tree_affinity": true, "preferred_altitude": 80}'::jsonb),
   
  -- Sky Hunters (high altitude specialists)
  ('owl', 'S🦅⭐K',
   ROW('#4682B4', '#87CEEB', '#B0E0E6'),
   '{"max_altitude": 250, "dive_speed": 2.5, "preferred_altitude": 200}'::jsonb),
   
  -- Cheese Mice (food motivated)
  ('mouse', 'C🐭🧀H',
   ROW('#FFD700', '#FFA500', '#FF8C00'),
   '{"food_attraction": 2.0, "speed": 0.8, "storage_behavior": true}'::jsonb),
   
  -- Field Mice (social)
  ('mouse', 'F🌾🌽D',
   ROW('#F5DEB3', '#DEB887', '#D2691E'),
   '{"flock_tendency": 0.9, "speed": 1.2, "group_size_preference": 5}'::jsonb),
   
  -- Rock Mice (solitary)
  ('mouse', 'R🪨🍄K',
   ROW('#696969', '#808080', '#A9A9A9'),
   '{"flock_tendency": 0.1, "camouflage": 0.7, "hiding_skill": 0.9}'::jsonb);
```

### Large Varied Population
```sql
-- Generate 500 creatures with rich variation
WITH creature_templates AS (
  SELECT * FROM (VALUES
    ('owl', ARRAY['🦉', '🦅', '🌙', '⭐', '🌲'], 0.2),
    ('mouse', ARRAY['🐭', '🧀', '🌾', '🌽', '🥜'], 0.6),
    ('duck', ARRAY['🦆', '💧', '🌊', '🏞️', '🪷'], 0.15),
    ('bee', ARRAY['🐝', '🌻', '🌺', '🌸', '🌼'], 0.05)
  ) AS t(species, emoji_set, spawn_weight)
),
color_palettes AS (
  SELECT * FROM (VALUES
    ('earth', '#8B4513', '#A0522D', '#D2691E'),
    ('sky', '#4682B4', '#87CEEB', '#B0E0E6'),
    ('forest', '#228B22', '#32CD32', '#90EE90'),
    ('sunset', '#FF4500', '#FF6347', '#FFA07A'),
    ('night', '#191970', '#4169E1', '#6495ED'),
    ('golden', '#FFD700', '#FFA500', '#FF8C00')
  ) AS t(palette_name, inner, middle, outer)
)
INSERT INTO creatures (species, wizzy_id, inner_color, middle_color, outer_color,
                      spawn_position, personality_seed)
SELECT
  species,
  -- Generate unique WIZZID
  CHR(65 + (creature_num % 26)) ||
  emoji_set[1 + (creature_num % array_length(emoji_set, 1))] ||
  emoji_set[1 + ((creature_num * 3) % array_length(emoji_set, 1))] ||
  CHR(65 + ((creature_num * 7 + 13) % 26)) ||
  -- Add number suffix if needed for uniqueness
  CASE WHEN creature_num > 260 THEN (creature_num / 260)::text ELSE '' END AS wizzy_id,
  
  -- Color selection
  cp.inner,
  cp.middle,
  cp.outer,
  
  -- Spawn in different regions
  point(
    CASE 
      WHEN species = 'duck' THEN 400 + random() * 200  -- Near water
      WHEN species = 'bee' THEN 200 + random() * 400   -- Gardens
      ELSE random() * 800                               -- Anywhere
    END,
    CASE
      WHEN species = 'duck' THEN 300 + random() * 100  -- Lake area
      ELSE random() * 600                               -- Anywhere
    END
  ) AS spawn_position,
  
  -- Personality seed for procedural behavior
  md5(creature_num::text || species)::uuid AS personality_seed
  
FROM (
  -- Generate creatures with weighted distribution
  SELECT 
    row_number() OVER () AS creature_num,
    species,
    emoji_set
  FROM generate_series(1, 500) n
  CROSS JOIN LATERAL (
    SELECT species, emoji_set
    FROM creature_templates
    WHERE random() < spawn_weight
    ORDER BY random()
    LIMIT 1
  ) selected_template
) creatures
CROSS JOIN LATERAL (
  SELECT * FROM color_palettes
  ORDER BY random()
  LIMIT 1
) cp;
```

### Scenario: Night Hunters vs Dawn Foragers
```sql
-- Create a specific ecological scenario
BEGIN;

-- Clear existing creatures
TRUNCATE TABLE creatures;

-- Spawn night hunter owls
INSERT INTO creatures (species, wizzy_id, colors, traits)
SELECT
  'owl',
  'N' || (ARRAY['🦉', '🌙', '⭐', '🌌'])[1 + (n % 4)] ||
  (ARRAY['🌙', '⭐', '🌌', '🦉'])[1 + ((n * 3) % 4)] || 
  CHR(65 + n % 26) AS wizzy_id,
  
  ROW('#191970', '#4169E1', '#87CEEB') AS colors,
  
  jsonb_build_object(
    'hunt_window', '[22, 23, 0, 1, 2, 3, 4, 5]',  -- Active hours
    'vision_multiplier', 2.5,
    'stealth', 0.9,
    'timezone', 'UTC-' || (n % 8)  -- Spread across night zones
  ) AS traits
FROM generate_series(1, 20) n;

-- Spawn dawn forager mice  
INSERT INTO creatures (species, wizzy_id, colors, traits)
SELECT
  'mouse',
  'D' || (ARRAY['🐭', '🌅', '🌾', '🌻'])[1 + (n % 4)] ||
  (ARRAY['🌻', '🌼', '🌺', '🌸'])[1 + ((n * 3) % 4)] ||
  CHR(65 + n % 26) AS wizzy_id,
  
  ROW('#FFD700', '#FFA500', '#FF8C00') AS colors,
  
  jsonb_build_object(
    'active_window', '[5, 6, 7, 8, 18, 19]',  -- Dawn/dusk
    'speed_multiplier', 1.5,
    'alertness', 0.95,
    'group_behavior', true
  ) AS traits
FROM generate_series(1, 100) n;

COMMIT;
```

## Cool Extension Ideas

### Weather-Affected Creatures
```sql
-- Creatures that respond to weather patterns
INSERT INTO weather_creatures (species, wizzy_id, weather_preferences)
VALUES
  ('owl', 'R🦉🌧️N', '{"rain": 1.2, "clear": 0.8, "fog": 1.5}'::jsonb),
  ('owl', 'S🦅☀️Y', '{"rain": 0.5, "clear": 1.5, "wind": 1.3}'::jsonb),
  ('mouse', 'W🐭☔T', '{"rain": 0.3, "clear": 1.0, "storm": 0.1}'::jsonb);
```

### Family Relationships
```sql
-- Creatures with family bonds (shared emojis = related)
INSERT INTO creatures_with_families (wizzy_id, family_emojis, relation_strength)
VALUES
  ('P🦉🌙A', ARRAY['🌙'], 1.0),  -- Parent
  ('C🦉🌙1', ARRAY['🌙'], 0.8),  -- Child 1  
  ('C🦉🌙2', ARRAY['🌙'], 0.8),  -- Child 2
  ('U🌲🌙Z', ARRAY['🌙'], 0.5);  -- Uncle (shares moon emoji)
```

### Seasonal Migrations
```sql
-- Creatures that migrate based on global time
INSERT INTO migratory_creatures (wizzy_id, summer_zone, winter_zone, migration_day)
SELECT
  'M' || (ARRAY['🦆', '🦢', '🕊️'])[1 + (n % 3)] ||
  '🌍' || CHR(65 + n) AS wizzy_id,
  'UTC+' || (n % 6) AS summer_zone,
  'UTC-' || (n % 6) AS winter_zone,
  90 + (n * 30) AS migration_day  -- Staggered migrations
FROM generate_series(1, 10) n;
```

---

*"With WIZZIDs and SQL, every creature becomes a unique story waiting to unfold!"* - The LLOOOOMM Database Poets 🦉📊✨ 