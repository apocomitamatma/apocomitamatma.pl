<script>
	import { Sprite } from '$lib/components';
	import imageUrl from '$lib/images/sprites/figures.png';
</script>

<Sprite {imageUrl} spriteId="figures" />

<style>
	:global(.sprite-image[data-sprite-id='figures']) {
		/*
        I'm not really happy about these;
        They're image-dependent

        Perhaps adjust the images
        */
		height: 105%;
		padding-left: 1%;
	}
</style>
