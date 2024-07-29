<script>
	import { Nav, Container, Footer } from '$lib/components';
</script>

<main>
	<div class="background"></div>
	<Nav />
	<Container>
		<slot />
	</Container>
	<Footer />
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
		overflow-x: hidden;
		background: black;
	}

	:global(main) {
		height: 100vh;
		font-size: x-large;
		text-align: justify;
	}

	:global(a) {
		color: var(--theme-blue);
		filter: brightness(150%);
		text-decoration: none;
	}

	:global(a):hover {
		filter: none;
	}

	:global(.section-name) {
		color: inherit;
		filter: none;
		text-decoration: inherit;
	}

	:global(.section-name):hover::after {
		content: ' 🔗';
		color: darkgrey;
	}

	.background {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background: url('$lib/images/background.png') center/cover fixed no-repeat;
		filter: brightness(20%);
		z-index: -1;
	}

	:global(main) {
		position: relative;
		z-index: 1;
	}
</style>
