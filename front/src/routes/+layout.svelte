<script>
	import { Nav, Container } from '$lib/components';
</script>

<main>
	<div class="background"></div>
	<Nav></Nav>
	<Container>
		<slot />
	</Container>
</main>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Albert+Sans:wght@400;700&display=swap');

	:global(:root) {
		--theme-yellow: #ffbf01;
		--theme-blue: #0173f8;
		--theme-red: #c50000;
		--max-page-width: 1424px;
	}

	:global(body) {
		font-family: 'Albert Sans', sans-serif;
		color: white;
		margin: 0;
		height: 100%;
		overflow-x: hidden;
		position: relative;
		background: black; /* Fallback color */
	}

	:global(main) {
		font-size: 2em;
	}

	.background {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background: url('$lib/images/background.png') center/cover fixed no-repeat;
		filter: blur(30px);
		z-index: -1;
	}

	:global(main) {
		position: relative;
		z-index: 1;
	}
</style>
