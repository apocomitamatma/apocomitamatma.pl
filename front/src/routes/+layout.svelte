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
		--layout-logotype-width: 300px;
		--layout-max-width: 1424px;
		--layout-padding-x: 5vw;
		--layout-padding-y: 40px;
		--layout-nav-padding-y: 0;
		--layout-nav-min-height: 100px;
		--layout-nav-border-width: 8px;
		--layout-nav-border-color: var(--theme-red);
		--layout-nav-border: var(--layout-nav-border-width) solid var(--layout-nav-border-color);
		--layout-nav-font-size: 1.1175rem;
		--layout-emp-font-size: 1.125rem;
	}

	:global(*) {
		box-sizing: border-box;
	}

	:global(html, body) {
		margin: 0;
		padding: 0;
		height: 100%;
	}

	:global(html) {
		font-size: large;
	}

	:global(body) {
		background: black;
	}

	:global(main) {
		font-family: 'Albert Sans', sans-serif;
		color: white;
		height: 100%;
		display: flex;
		overflow-x: hidden;
		flex-direction: column;
		text-align: justify;
	}

	:global(a) {
		color: var(--theme-blue);
		filter: brightness(180%);
		text-decoration: none;
	}

	:global(a):hover {
		filter: brightness(150%);
	}

	:global(.section-name) {
		scroll-margin-top: 20px;
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
		width: 100%;
		height: 100%;
		height: 100svh;
		background: url('$lib/images/background.png') center/cover fixed repeat;
		filter: brightness(15%);
		z-index: -1;
	}
</style>
