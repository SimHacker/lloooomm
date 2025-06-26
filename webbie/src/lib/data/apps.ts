export interface App {
	id: string;
	title: string;
	description: string;
	route: string;
	status: 'live' | 'coming-soon' | 'prototype';
	tags: string[];
	featured?: boolean;
}

export const apps: App[] = [
	{
		id: 'hacker-news-leela-lloooomm',
		title: 'Hacker News LLOOOOMM Discussion',
		description: 'Complete simulated HN thread exploring AI-Human Collaborative Intelligence. Features Rush Limbaugh\'s transformation, grammar nazi civil wars, X-Files debugging stories, and deep technical discussions spanning 12 pages.',
		route: '/hacker-news-leela-lloooomm',
		status: 'live',
		tags: ['AI', 'Hacker News', 'Character Simulation', 'LLOOOOMM'],
		featured: true
	},
	{
		id: 'coming-soon-1',
		title: 'Star Trek Academy DevOps',
		description: 'Learn infrastructure management at Starfleet Academy with Captain Picard, Data, and Geordi La Forge as your instructors.',
		route: '/star-trek-devops',
		status: 'coming-soon',
		tags: ['Star Trek', 'DevOps', 'Education']
	},
	{
		id: 'coming-soon-2',
		title: 'X-Files System Debugging',
		description: 'Investigate mysterious system failures with Mulder and Scully. The truth is out there... in your logs.',
		route: '/x-files-debugging',
		status: 'coming-soon',
		tags: ['X-Files', 'Debugging', 'Mystery']
	},
	{
		id: 'coming-soon-3',
		title: 'Mr. Rogers\' Neighborhood APIs',
		description: 'Learn API design and documentation with the kindest teacher in tech. Won\'t you be my API neighbor?',
		route: '/mr-rogers-apis',
		status: 'coming-soon',
		tags: ['Mr. Rogers', 'APIs', 'Documentation', 'Kindness']
	}
]; 