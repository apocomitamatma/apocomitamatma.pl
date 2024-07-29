<script>
	import { onMount } from 'svelte';

	import statistics from '$lib/statistics.json';

	/**
	 * @type {'e8' | 'mp' | 'mr'}
	 */
	export let category;

	const videoCounts = statistics.videoCount;
	export const videoCount = videoCounts[category];
	const roundedVideoCount = Math.round(videoCount / 10) * 10;
	export const videoCountForDisplay =
		roundedVideoCount.toString() + (videoCount % 10 == 0 ? '' : '+');
</script>

{videoCountForDisplay}
