<script>
	import '../reset.css';
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
		--layout-padding-x: min(5vw, 25px);
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

	:global(h1, h2, h3) /* h4, h5, h6 */ {
		color: var(--theme-yellow);
	}

	:global(.section-name) {
		scroll-margin-top: 20px;
		filter: brightness(180%);
		color: inherit;
		filter: none;
		text-decoration: inherit;
	}

	:global(.section-name):hover::after {
		filter: brightness(180%);
	}

	:global(.section-name):hover::after {
		content: ' 🔗';
		color: darkgrey;
	}

	/* For objects to take up whole vh on load (PC screens only) */
	:global(#entry) {
		min-height: 420px;
		/*
		I had an idea of making a flexbox that would only include the nav and landing
		but that conflicts heavily with the layout defined in `+layout.svelte`.

		As a trade-off, we're calculating the height of the landing to be 100vh
		in most browsers using the *red-flag* formula below.
		*/
		height: calc(100vh - var(--layout-nav-min-height) - var(--layout-padding-y) - 35px);
		max-height: 900px;
	}

	@media (max-width: 1100px) {
		:global(#entry) {
			height: unset;
		}
	}

	.background {
		position: fixed;
		width: 100%;
		height: 100%;
		height: 100svh;
		background: url('$lib/images/background.png') center/cover fixed repeat;
		filter: blur(5px) brightness(50%);
		z-index: -1;
	}
</style>
