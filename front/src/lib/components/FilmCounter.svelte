<script>
	import statistics from '$lib/statistics.json';

	/**
	 * @type {{omen: 'E8' | 'MP' | 'MR'}}
	 */
	let { omen } = $props();

	const videoCounts = statistics.videoCount;
	export const videoCount = videoCounts[omen];
	const roundedVideoCount = Math.round(videoCount / 10) * 10;
	export const videoCountForDisplay =
		roundedVideoCount.toString() + (videoCount % 10 == 0 ? '' : '+');
</script>

{videoCountForDisplay}
