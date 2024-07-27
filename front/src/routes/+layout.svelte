<script>
	import Nav from './Nav.svelte';
</script>

<main>
	<Nav></Nav>
	<slot />
</main>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Albert+Sans:wght@400;700&display=swap');

	:global(:root) {
		--theme-yellow: #ffbf01;
		--theme-blue: #0173f8;
		--theme-red: #c50000;
	}

	:global(body) {
		font-family: 'Albert Sans', sans-serif;
		color: white;
		background: url('$lib/images/background.png') center/cover fixed no-repeat;
		margin: 0;
		height: 100%;
		overflow-x: hidden;
	}
</style>
