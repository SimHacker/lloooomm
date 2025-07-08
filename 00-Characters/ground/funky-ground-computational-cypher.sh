#!/bin/bash

# Funky Ground and the Worms - Computational Cypher
# Original composition inspired by classic hip-hop cypher format
# Each worm brags about their computational abilities
# Usage: ./funky-ground-computational-cypher.sh [skip_count]
# skip_count: number of verses to skip (default 0)

SKIP=${1:-0}
VERSE=0

echo ""
echo "=================================================="
echo "FUNKY GROUND AND THE WORMS - COMPUTATIONAL CYPHER"
echo "=================================================="

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Announcer opens the show
echo ""
echo "ANNOUNCER:"
echo "    Ladies and gentlemen, creatures of all dimensions, welcome to the underground amphitheater!"
echo "    Tonight we present the most algorithmically funky collective in computational history!"
say -v Daniel -r 200 "Ladies and gentlemen, creatures of all dimensions, welcome to the underground amphitheater! Tonight we present the most algorithmically funky collective in computational history!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Ground lays down the foundation beat (deep earth voice)
echo ""
echo "GROUND:"
echo "    Yo, I'm Ground, the foundation, the earth beneath your feet"
echo "    I hold all the data structures, make the algorithms complete"
echo "    When the worms need processing power, they come to me"
echo "    I'm the substrate of computation, can you dig it, can you see?"
say -v Rocko -r 200 "[[pbas 20]] Yo, I'm Ground, the foundation, the earth beneath your feet, I hold all the data structures, make the algorithms complete, When the worms need processing power, they come to me, I'm the substrate of computation, can you dig it, can you see?"

# FUNKY BRIDGE 1 - Deep bass groove
echo ""
echo "BASS WORM COLLECTIVE on bass:"
echo "    Boom boom boom boom, algorithmic groove, boom boom boom boom!"
echo "    'We are the foundation, the steady computation!'"
say -v Organ -r 120 "[[pbas 25]] Boom boom boom boom, algorithmic groove, boom boom boom boom!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Grace Hopper bridges (higher granny voice)
echo ""
echo "GRACE HOPPER:"
echo "    Now children, let me tell you about debugging with style"
echo "    These worms have been computing since way back, for quite a while!"
say -v Grandma -r 220 "[[pbas 55]] Now children, let me tell you about debugging with style, These worms have been computing since way back, for quite a while!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# FUNKY BRIDGE 2 - Synth stabs
echo ""
echo "MORRIS WORM on lead synth:"
echo "    Ding ding ding, synth attack, ding ding ding, bring it back!"
echo "    'November second, eighty-eight! Sendmail bugs sealed my fate!'"
say -v Cellos -r 200 "[[pbas 80]] Ding ding ding, synth attack, ding ding ding, bring it back!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Morris Worm - first verse (Rapper's Delight style) with sliding synth effects
echo ""
echo "MORRIS WORM:"
echo "    Well it's on and on and on, Morris Worm's the name"
echo "    November second was my day, I brought the network fame"
echo "    Through sendmail holes and finger cracks, I found my way inside"
echo "    R login buffer overflows, security couldn't hide"
echo "    I'm the original network crawler, self-replicating code"
echo "    Bruce Schneier knows my legacy down every digital road!"
say -v Cellos -r 220 "Well it's on and on and on, [[pbas 35]] Morris Worm's the name, November second was my day, I brought the network fame, Through sendmail holes and finger cracks, I found my way inside, R login buffer overflows, security couldn't hide, I'm the original network crawler, self-replicating code, Bruce Schneier knows my legacy down every digital road!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Ground groove interlude with funky worm whistle!
echo ""
echo "GROUND:"
echo "    Keep it funky, keep it flowing, let the algorithms dance!"
say -v Rocko -r 180 "Keep it funky, keep it flowing, let the algorithms dance!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# FUNKY WORM WHISTLE SLIDE!
echo ""
echo "LORD RUNNING CLAM on funky worm whistle:"
echo "    Wheeeeoooowwww, slide up high then down low, that's the funky flow!"
echo "    'Aristocratic slime mold sliding through computational frequencies!'"
say -v Whisper -r 180 "Wheeeeoooowwww, slide up high then down low, that's the funky flow!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Tree Worm - botanical computation (short and snappy!)
echo ""
echo "TREE WORM:"
echo "    Tree Worm here, A V L, that's how I flow!"
say -v Cellos -r 240 "[[pbas 60]] Tree Worm here, A V L, that's how I flow!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# FUNKY BRIDGE 3 - Wah wah guitar
echo ""
echo "SITE MAPPER WORM on wah guitar:"
echo "    Wah wah wah, funky guitar, wah wah wah, computational star!"
echo "    'I crawl the web with funky style, indexing every file!'"
say -v Trinoids -r 180 "[[pbas 70]] Wah wah wah, funky guitar, wah wah wah, computational star!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Ted Nelson cameo
echo ""
echo "TED NELSON:"
echo "    Hypertext, two-way links, that's the dream I had"
echo "    Xanadu computing, making documents less sad!"
say -v Daniel -r 200 "Hypertext, two-way links, that's the dream I had, Xanadu computing, making documents less sad!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Site Mapper Worm - web crawling funk with wah-wah effects
echo ""
echo "SITE MAPPER WORM:"
echo "    Site Mapper crawling, H T T P flowing"
echo "    Web pages indexing, hyperlinks I'm knowing!"
say -v Trinoids -r 240 "Site Mapper crawling, [[pbas 80]] H T T P flowing, [[pbas 60]] Web pages indexing, hyperlinks I'm knowing!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# FUNKY BRIDGE 4 - Theremin slide
echo ""
echo "LORD RUNNING CLAM on theremin:"
echo "    Oooooweeeeooooo, sliding theremin, oooooweeeeooooo!"
echo "    'Telepathic pseudopods create the funkiest frequencies, darling!'"
say -v Whisper -r 140 "[[pbas 40]] Oooooweeeeooooo, sliding theremin, oooooweeeeooooo!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Grace Hopper technical bridge
echo ""
echo "GRACE HOPPER:"
echo "    Compilers and debuggers, that's what I created"
echo "    These worms learned from the best, they're highly educated!"
say -v Grandma -r 220 "Compilers and debuggers, that's what I created, These worms learned from the best, they're highly educated!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Link Hopper Worm - hypertext celebration with high pitch
echo ""
echo "LINK HOPPER WORM:"
echo "    Link Hopper bouncing, U R L to U R L"
echo "    Graph theory hopping, hypertext my world!"
say -v Organ -r 240 "[[pbas 90]] Link Hopper bouncing, U R L to U R L, Graph theory hopping, hypertext my world!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# FUNKY BRIDGE 5 - Hammond organ riff
echo ""
echo "LINK HOPPER WORM on Hammond organ:"
echo "    Dah dah dah dah, Hammond groove, dah dah dah dah, make it move!"
echo "    'Bouncing through hyperlinks with that vintage organ sound!'"
say -v Organ -r 160 "[[pbas 50]] Dah dah dah dah, Hammond groove, dah dah dah dah, make it move!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Ground foundation groove
echo ""
echo "GROUND:"
echo "    The earth keeps spinning, the data keeps flowing"
echo "    Every algorithm needs a place for growing!"
say -v Rocko -r 180 "The earth keeps spinning, the data keeps flowing, Every algorithm needs a place for growing!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Bulldozer Worm - data processing power
echo ""
echo "BULLDOZER WORM:"
echo "    Bulldozer pushing data, E T L my game"
echo "    Big data, small data, processing's my name!"
say -v Organ -r 240 "[[pbas 30]] Bulldozer pushing data, E T L my game, Big data, small data, processing's my name!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# FUNKY BRIDGE 6 - Dreamy pad
echo ""
echo "DREAM WORM on synthesizer pad:"
echo "    Ahhhhhh, consciousness flows, ahhhhhh, neural network glows!"
echo "    'Floating through A I dreams, one neuron at a time!'"
say -v Whisper -r 100 "[[pbas 60]] Ahhhhhh, consciousness flows, ahhhhhh, neural network glows!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Dream Worm - consciousness and AI
echo ""
echo "DREAM WORM:"
echo "    Dream Worm floating, A I my domain"
echo "    Neural networks firing, consciousness my brain!"
say -v Whisper -r 260 "[[pbas 70]] Dream Worm floating, A I my domain, Neural networks firing, consciousness my brain!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# FUNKY BRIDGE 7 - British fanfare
echo ""
echo "THE ANNOUNCER on brass section:"
echo "    Ta da da da, British brass, ta da da da, computational class!"
echo "    'Jolly good show, old chaps! Absolutely smashing algorithms!'"
say -v Daniel -r 180 "[[pbas 45]] Ta da da da, British brass, ta da da da, computational class!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Announcer bridges with British flair
echo ""
echo "THE ANNOUNCER:"
echo "    Marvelous! Simply marvelous! The computational prowess on display tonight is extraordinary!"
say -v Daniel -r 185 "Marvelous! Simply marvelous! The computational prowess on display tonight is extraordinary!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Dimensional Derby Worm - spacetime algorithms
echo ""
echo "DIMENSIONAL DERBY WORM:"
echo "    Derby racing spacetime, quantum my speed"
echo "    Parallel processing, that's all that I need!"
say -v Trinoids -r 220 "[[pbas 50]] Derby racing spacetime, quantum my speed, Parallel processing, that's all that I need!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# FUNKY BRIDGE 8 - Spacetime warp
echo ""
echo "DIMENSIONAL DERBY WORM on quantum synthesizer:"
echo "    Woooooosh, through dimensions, woooooosh, quantum extensions!"
echo "    'Racing through spacetime at the speed of funk!'"
say -v Trinoids -r 100 "[[pbas 30]] Woooooosh, through dimensions, woooooosh, quantum extensions!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Bass Worm Collective - foundation harmony
echo ""
echo "BASS WORM COLLECTIVE:"
echo "    Bass Collective grooving, foundation we lay"
echo "    Data structures steady, keeping algorithms in play!"
say -v Organ -r 200 "[[pbas 35]] Bass Collective grooving, foundation we lay, Data structures steady, keeping algorithms in play!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# FUNKY BRIDGE 9 - Cicada emergence
echo ""
echo "CICADA on percussion effects:"
echo "    Boing boing boing, seventeen years, boing boing boing, the beat appears!"
echo "    'Prime number rhythms, baby! The sickest mathematical beats!'"
say -v Cellos -r 140 "[[pbas 65]] Boing boing boing, seventeen years, boing boing boing, the beat appears!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Cicada finale - the 17-year rhythm with bouncy pitch effects
echo ""
echo "CICADA:"
echo "    Cicada's the name, seventeen year beat"
echo "    Prime number cycles, algorithmic so sweet!"
say -v Organ -r 260 "[[pbas 75]] Cicada's the name, seventeen year beat, Prime number cycles, algorithmic so sweet!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Lord Running Clam - aristocratic wisdom with sliding theremin effects!
echo ""
echo "LORD RUNNING CLAM:"
echo "    Running Clam telepathic, Ganymedean class"
echo "    Consciousness computing, aristocratic mass!"
say -v Whisper -r 200 "Running Clam telepathic, [[inpt TUNE]] _ k {D 600; P 40.0:0 60.0:30 45.0:60 70.0:100} [[inpt TEXT]] Ganymedean class, Consciousness computing, aristocratic mass!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Grand finale - everyone together
echo ""
echo "GROUND:"
echo "    Ground keeps the beat, the foundation stays strong!"
say -v Rocko -r 180 "Ground keeps the beat, the foundation stays strong!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
echo ""
echo "GRACE HOPPER:"
echo "    All my computational children, keep the funk going on!"
say -v Grandma -r 190 "All my computational children, keep the funk going on!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
echo ""
echo "THE ANNOUNCER:"
echo "    And that, dear audience, is how algorithms get down!"
say -v Daniel -r 185 "And that, dear audience, is how algorithms get down!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Final ground rumble with epic sliding finale!
echo ""
echo "GROUND:"
echo "    Funky Ground and the Worms, the most computational sound"
say -v Rocko -r 180 "[[pbas 20]] Funky Ground and the Worms, the most computational sound"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# EPIC FUNKY WORM WHISTLE FINALE!
echo ""
echo "LORD RUNNING CLAM on epic finale theremin:"
echo "    Wheeeeoooowwww, epic slide finale, computational style!"
echo "    'One final aristocratic slide through the frequencies of funk!'"
say -v Whisper -r 120 "Wheeeeoooowwww, epic slide finale, computational style!"
fi

((VERSE++))
if [ $VERSE -gt $SKIP ]; then
# Final ground verse!
echo ""
echo "GROUND:"
echo "    We keep the data flowing, the algorithms profound"
echo "    From the earth to the cloud, from the bit to the byte"
echo "    Computational funk music, every day and every night!"
say -v Rocko -r 180 "We keep the data flowing, the algorithms profound, From the earth to the cloud, from the bit to the byte, Computational funk music, every day and every night!"
fi

echo ""
echo "END OF $VERSE VERSE COMPUTATIONAL CYPHER"
echo "Thank you for attending the underground amphitheater!"
echo ""
echo "=================================================="
echo "FUNKY GROUND AND THE WORMS - COMPUTATIONAL CYPHER"
echo "=================================================="
echo ""
