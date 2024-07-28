<script>
	import { onMount } from 'svelte';
	let currentIndex = 0;
	/**
	 * @type {any[]}
	 */
	let items = [];

	// To capture the items from the slot
	/**
	 * @type {HTMLDivElement}
	 */
	let slots;

	onMount(() => {
		items = Array.from(slots.children);
		showItem(currentIndex);
	});

	/**
	 * @param {number} index
	 */
	function showItem(index) {
		items.forEach((item, i) => {
			item.style.display = i === index ? 'block' : 'none';
		});
	}

	function next() {
		currentIndex = (currentIndex + 1) % items.length;
		showItem(currentIndex);
	}

	setInterval(next, 3000);
</script>

<div class="carousel">
	<div class="carousel-inner" bind:this={slots}>
		<slot></slot>
	</div>
</div>

<style>
	.carousel {
		position: relative;
		width: 100%;
		margin: auto;
		overflow: hidden;
	}
	.carousel-inner {
		display: flex;
		flex-direction: column;
	}
	.carousel-inner > * {
		display: none;
		width: 100%;
	}
</style>
