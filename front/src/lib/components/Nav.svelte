<script>
	import { faDiscord, faYoutube, faFacebook, faTiktok } from '@fortawesome/free-brands-svg-icons';
	import Icon from './Icon.svelte';

	let isMenuOpen = $state(false);
	let toggleMenuSymbol = $derived(
		isMenuOpen ? '<span style="filter: brightness(50%);">☰</span>' : '☰'
	);

	function toggleMenu() {
		isMenuOpen = !isMenuOpen;
	}
</script>

<div class="nav-wrapper">
	<nav class="nav">
		<div class="nav-left">
			<a href="/" class="website-name"> </a>
		</div>
		<div class="nav-center" class:is-open={isMenuOpen}>
			<a href="/" class="nav-button">Początek</a>
			<a href="/films" class="nav-button">Filmy</a>
			<a href="/faq" class="nav-button">FAQ</a>
			<a href="/contact" class="nav-button">Kontakt</a>
		</div>
		<div class="nav-right" class:is-open={isMenuOpen}>
			<a href="/youtube" target="_blank" rel="noopener noreferrer"><Icon icon={faYoutube} /></a>
			<a href="/discord" target="_blank" rel="noopener noreferrer"><Icon icon={faDiscord} /></a>
			<a href="/tiktok" target="_blank" rel="noopener noreferrer"><Icon icon={faTiktok} /></a>
			<a href="/facebook" target="_blank" rel="noopener noreferrer"><Icon icon={faFacebook} /></a>
		</div>
		<div class="menu-toggle">
			<button onclick={toggleMenu}>{@html toggleMenuSymbol}</button>
		</div>
	</nav>
</div>

<style>
	.nav-wrapper {
		border-bottom: var(--layout-nav-border);
		backdrop-filter: brightness(30%);
		background-color: rgba(0, 0, 0, 0.2);
	}

	.nav {
		min-height: var(--layout-nav-min-height);
		max-width: var(--layout-max-width);
		padding-inline: var(--layout-padding-x);
		padding-top: var(--layout-nav-padding-y);
		padding-bottom: var(--layout-nav-padding-y);
		margin-inline: auto;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.nav-left,
	.nav-center,
	.nav-right {
		flex: 1;
		display: flex;
		align-items: center;
	}

	.website-name {
		height: var(--layout-nav-min-height);
		width: 80%;
		min-width: var(--layout-logotype-width);
		background-image: url('$lib/images/name.gif');
		background-size: contain;
		background-repeat: no-repeat;
		background-position: center;
	}

	.nav-center {
		justify-content: center;
		gap: 20px;
	}

	.nav-right {
		justify-content: flex-end;
		gap: 30px; /* Increased gap between social icons */
	}

	.nav-button {
		font-size: var(--layout-nav-font-size);
		text-decoration: none;
		color: inherit;
		padding: 10px;
		background: none;
		cursor: pointer;
		position: relative;
		overflow: hidden;
		transition: color 0.3s ease;
	}

	.nav-button:hover {
		color: var(--theme-yellow);
	}

	.nav-right a {
		color: inherit;
	}

	.menu-toggle {
		display: none;
	}

	@media (max-width: 1210px) {
		.nav {
			flex-direction: column;
			align-items: center;
			gap: 25px;
		}

		.website-name {
			min-width: 240px;
			width: 35%;
			background-position: center;
		}

		.nav-left,
		.nav-center,
		.nav-right {
			width: 100%;
			justify-content: center;
		}

		.nav-left {
			justify-content: left;
		}

		.nav-center {
			flex-direction: column;
		}

		.nav-center,
		.nav-right {
			display: none;
			align-items: center;
		}

		.nav-right {
			margin-top: 20px;
			margin-bottom: 40px;
		}

		.nav-center.is-open,
		.nav-right.is-open {
			display: flex;
		}

		.menu-toggle {
			display: block;
			position: absolute;
			right: var(--layout-padding-x);
			transform: translate(5px, 100%);
		}

		.menu-toggle button {
			font-size: 25px; /* In pixels since it's a navigation icon */
			border: none;
			/* border-width: 8px;
			border-color: var(--theme-red);
			border-radius: 20%; */
			color: var(--theme-yellow);
			background: transparent;
		}

		.menu-toggle button:hover {
			cursor: pointer;
		}
	}
</style>
