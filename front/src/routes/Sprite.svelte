<script>
	export let imageUrl;
	export let borderColor = 'var(--theme-blue)'; // Default border color set to blue
	export let borderWidth = '8px';
	export let size = '800px';
</script>

<div
	class="sprite-container"
	style="--border-color: {borderColor}; --border-width: {borderWidth}; --size: {size}"
>
	<!-- svelte-ignore a11y_img_redundant_alt -->
	<img src={imageUrl} alt="Sprite image" class="sprite-image" />
</div>

<style>
	.sprite-container {
		width: var(--size);
		height: var(--size);
		border-radius: 50%;
		backdrop-filter: brightness(50%) blur(17px);
		border: var(--border-width) solid var(--border-color);
		display: flex;
		align-items: center;
		justify-content: center;
		overflow: hidden;
	}

	.sprite-image {
		width: 100%;
		height: 100%;
		object-fit: contain;
		border-radius: 50%;
	}
</style>
