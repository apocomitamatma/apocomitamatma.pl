<script>
	/** @type{ {imageUrl: string, spriteId?: 'rizz' | 'figures' | 'delta' | 'unset'} }*/
	let { imageUrl, spriteId = 'unset' } = $props();
</script>

<!-- svelte-ignore a11y_img_redundant_alt -->
<img src={imageUrl} alt="Sprite image" class="sprite-image" data-sprite-id={spriteId} />

<style>
	.sprite-image {
		width: 100%;
		height: 90%;
		object-fit: contain;
		z-index: -1;
	}
</style>
