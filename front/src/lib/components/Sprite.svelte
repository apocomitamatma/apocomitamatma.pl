<script>
	export let imageUrl;
	export let spriteId = 'unset';
</script>

<!-- svelte-ignore a11y_img_redundant_alt -->
<img src={imageUrl} alt="Sprite image" class="sprite-image" data-sprite-id={spriteId} />

<style>
	.sprite-image {
		backdrop-filter: brightness(50%) blur(17px);
		width: 100%;
		height: 90%;
		object-fit: contain;
		box-shadow: 0px 0px 35px 35px rgba(0, 0, 0, 1);
		z-index: -1;
	}
</style>
