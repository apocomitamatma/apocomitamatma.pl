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
	<nav class="nav" data-is-open={isMenuOpen}>
		<div class="nav-left">
			<a href="/" class="website-name"> </a>
		</div>
		<div class="nav-center" data-is-open={isMenuOpen}>
			<a href="/" class="nav-button">Początek</a>
			<a href="/films" class="nav-button">Filmy</a>
			<a href="/faq" class="nav-button">FAQ</a>
			<a href="/contact" class="nav-button">Kontakt</a>
		</div>
		<div class="nav-right" data-is-open={isMenuOpen}>
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

	@media (max-width: 1030px) {
		.nav {
			flex-direction: column;
			align-items: center;
			gap: 2rem;
		}

		.nav[data-is-open='true'] {
			margin-bottom: 2rem;
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

		.nav-center[data-is-open='true'],
		.nav-right[data-is-open='true'] {
			display: flex;
		}

		.menu-toggle {
			display: block;
			position: absolute;
			right: var(--layout-padding-x);
		}

		.menu-toggle button {
			font-size: 3.5rem;
			border: none;
			color: var(--theme-yellow);
			background: transparent;
		}

		.menu-toggle button:hover {
			cursor: pointer;
		}
	}
</style>
