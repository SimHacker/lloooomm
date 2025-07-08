<script lang="ts">
	import { onMount } from 'svelte';
	
	interface App {
		id: string;
		title: string;
		description: string;
		route: string;
		status: 'live' | 'coming-soon' | 'prototype';
		tags: string[];
		featured?: boolean;
	}
	
	const apps: App[] = [
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
	
	let mounted = false;
	
	onMount(() => {
		mounted = true;
	});
</script>

<svelte:head>
	<title>LLOOOOMM Apps - AI-Human Collaborative Intelligence Platform</title>
	<meta name="description" content="Self-contained interactive applications showcasing LLOOOOMM's character simulation and narrative-driven learning." />
</svelte:head>

<div class="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50">
	<!-- Header -->
	<header class="bg-white shadow-sm border-b border-slate-200">
		<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
			<div class="flex items-center justify-between">
				<div>
					<h1 class="text-3xl font-bold text-slate-900">LLOOOOMM Apps</h1>
					<p class="text-slate-600 mt-1">AI-Human Collaborative Intelligence Platform</p>
				</div>
				<div class="text-right">
					<div class="text-sm text-slate-500">Character Simulation</div>
					<div class="text-sm text-slate-500">Narrative Learning</div>
					<div class="text-sm text-slate-500">Interactive Adventures</div>
				</div>
			</div>
		</div>
	</header>

	<!-- Main Content -->
	<main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
		<!-- Featured App -->
		{#each apps.filter(app => app.featured) as app}
			<section class="mb-16">
				<div class="bg-white rounded-xl shadow-lg border border-slate-200 overflow-hidden">
					<div class="bg-gradient-to-r from-orange-500 to-red-500 px-8 py-6">
						<div class="flex items-center justify-between">
							<div>
								<h2 class="text-2xl font-bold text-white">{app.title}</h2>
								<div class="flex items-center gap-2 mt-2">
									<span class="bg-white/20 text-white px-2 py-1 rounded text-sm font-medium">Featured</span>
									<span class="bg-green-500 text-white px-2 py-1 rounded text-sm font-medium">Live</span>
								</div>
							</div>
							<div class="text-white/80 text-sm">
								<div>🧠 Character Simulation</div>
								<div>💬 Realistic HN Discussion</div>
								<div>⚡ Interactive Navigation</div>
							</div>
						</div>
					</div>
					
					<div class="p-8">
						<p class="text-slate-700 text-lg leading-relaxed mb-6">{app.description}</p>
						
						<div class="flex flex-wrap gap-2 mb-6">
							{#each app.tags as tag}
								<span class="bg-slate-100 text-slate-700 px-3 py-1 rounded-full text-sm">{tag}</span>
							{/each}
						</div>
						
						<div class="flex gap-4">
							<a 
								href={app.route}
								class="bg-orange-500 hover:bg-orange-600 text-white px-6 py-3 rounded-lg font-medium transition-colors duration-200 flex items-center gap-2"
							>
								🚀 Launch App
							</a>
							<button class="bg-slate-100 hover:bg-slate-200 text-slate-700 px-6 py-3 rounded-lg font-medium transition-colors duration-200">
								📖 View Documentation
							</button>
						</div>
					</div>
				</div>
			</section>
		{/each}

		<!-- All Apps Grid -->
		<section>
			<h2 class="text-2xl font-bold text-slate-900 mb-8">All Applications</h2>
			
			<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
				{#each apps as app}
					<div class="bg-white rounded-lg shadow-md border border-slate-200 overflow-hidden hover:shadow-lg transition-shadow duration-200">
						<div class="p-6">
							<div class="flex items-start justify-between mb-3">
								<h3 class="text-xl font-semibold text-slate-900">{app.title}</h3>
								<span class="px-2 py-1 rounded text-xs font-medium {
									app.status === 'live' ? 'bg-green-100 text-green-800' :
									app.status === 'prototype' ? 'bg-yellow-100 text-yellow-800' :
									'bg-slate-100 text-slate-600'
								}">
									{app.status === 'live' ? 'Live' : 
									 app.status === 'prototype' ? 'Prototype' : 
									 'Coming Soon'}
								</span>
							</div>
							
							<p class="text-slate-600 text-sm mb-4 line-clamp-3">{app.description}</p>
							
							<div class="flex flex-wrap gap-1 mb-4">
								{#each app.tags.slice(0, 3) as tag}
									<span class="bg-slate-100 text-slate-600 px-2 py-1 rounded text-xs">{tag}</span>
								{/each}
								{#if app.tags.length > 3}
									<span class="text-slate-400 text-xs">+{app.tags.length - 3} more</span>
								{/if}
							</div>
							
							<div class="flex gap-2">
								{#if app.status === 'live'}
									<a 
										href={app.route}
										class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded text-sm font-medium transition-colors duration-200 flex-1 text-center"
									>
										Launch
									</a>
								{:else}
									<button 
										disabled
										class="bg-slate-200 text-slate-500 px-4 py-2 rounded text-sm font-medium flex-1 cursor-not-allowed"
									>
										{app.status === 'prototype' ? 'Preview Soon' : 'Coming Soon'}
									</button>
								{/if}
							</div>
						</div>
					</div>
				{/each}
			</div>
		</section>

		<!-- About Section -->
		<section class="mt-16 bg-slate-900 rounded-xl p-8 text-white">
			<h2 class="text-2xl font-bold mb-4">About LLOOOOMM</h2>
			<div class="grid md:grid-cols-2 gap-8">
				<div>
					<h3 class="text-lg font-semibold mb-2 text-blue-300">Character Simulation</h3>
					<p class="text-slate-300 text-sm">
						Multiple AI characters with distinct personalities collaborate on complex problems, 
						implementing Marvin Minsky's "Society of Mind" theory at production scale.
					</p>
				</div>
				<div>
					<h3 class="text-lg font-semibold mb-2 text-green-300">Narrative Learning</h3>
					<p class="text-slate-300 text-sm">
						Transform technical documentation into interactive adventures. 
						Debugging becomes detective work, learning becomes storytelling.
					</p>
				</div>
				<div>
					<h3 class="text-lg font-semibold mb-2 text-purple-300">Universal Themes</h3>
					<p class="text-slate-300 text-sm">
						Adapt any fictional universe into educational experiences. 
						Star Trek for DevOps, X-Files for debugging, Mr. Rogers for APIs.
					</p>
				</div>
				<div>
					<h3 class="text-lg font-semibold mb-2 text-orange-300">Production Ready</h3>
					<p class="text-slate-300 text-sm">
						Real infrastructure management with collaborative intelligence. 
						Multi-GCP deployments, incident response, and knowledge transfer.
					</p>
				</div>
			</div>
		</section>
	</main>

	<!-- Footer -->
	<footer class="bg-white border-t border-slate-200 mt-16">
		<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
			<div class="text-center text-slate-600">
				<p class="text-sm">
					LLOOOOMM - Where AI characters collaborate and humans learn through narrative
				</p>
				<p class="text-xs mt-2">
					Built with SvelteKit • Character Simulation • Narrative Intelligence
				</p>
			</div>
		</div>
	</footer>
</div>

<style>
	.line-clamp-3 {
		display: -webkit-box;
		-webkit-line-clamp: 3;
		-webkit-box-orient: vertical;
		overflow: hidden;
	}
</style>
