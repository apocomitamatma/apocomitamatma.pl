<script>
	import { faDiscord, faYoutube, faFacebook, faTiktok } from '@fortawesome/free-brands-svg-icons';
	import Icon from './Icon.svelte';

	let isMenuOpen = false;
	$: toggleMenuSymbol = isMenuOpen ? '<span style="filter: brightness(50%);">☰</span>' : '☰';

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
			<a href="/discord" target="_blank" rel="noopener noreferrer"><Icon icon={faDiscord} /></a>
			<a href="/youtube" target="_blank" rel="noopener noreferrer"><Icon icon={faYoutube} /></a>
			<a href="/facebook" target="_blank" rel="noopener noreferrer"><Icon icon={faFacebook} /></a>
			<a href="/tiktok" target="_blank" rel="noopener noreferrer"><Icon icon={faTiktok} /></a>
		</div>
		<div class="menu-toggle">
			<button on:click={toggleMenu}>{@html toggleMenuSymbol}</button>
		</div>
	</nav>
</div>

<style>
	:root {
		--nav-min-height: 100px;
	}

	.nav-wrapper {
		border-bottom: 8px solid var(--theme-red);
		padding: 15px;
		backdrop-filter: brightness(30%);
		background-color: rgba(0, 0, 0, 0.2);
	}

	.nav {
		min-height: var(--nav-min-height);
		max-width: var(--max-page-width);
		margin-left: auto;
		margin-right: auto;
		padding-left: 5vw;
		padding-right: 5vw;
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
		height: 100px;
		top: 50%;
		width: 80%;
		min-width: 200px;
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
		text-decoration: none;
		color: inherit;
		padding: 10px;
		background: none;
		cursor: pointer;
		font-size: 24px;
		position: relative;
		overflow: hidden;
		transition: color 0.3s ease;
	}

	.nav-button:hover {
		color: var(--theme-yellow);
	}

	.nav-right a {
		color: inherit;
		font-size: 24px;
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
			min-width: 300px;
			width: 50%;
			background-position: center;
		}

		.nav-left,
		.nav-center,
		.nav-right {
			width: 100%;
			justify-content: center;
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
			margin-bottom: 20px;
		}

		.nav-center.is-open,
		.nav-right.is-open {
			display: flex;
		}

		.menu-toggle {
			display: block;
			position: absolute;
			top: calc((var(--nav-min-height) + 30px) / 2);
			margin-top: -30px;
			margin-bottom: -15px;
			right: 15px;
		}

		.menu-toggle button {
			font-size: 1.5em;
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

	@media (max-width: 605px) {
		.website-name {
			background-position: left;
		}
		.nav-left {
			justify-content: left;
		}
	}
}
</style>
