<script>
	import { faDiscord, faYoutube, faFacebook, faTiktok } from '@fortawesome/free-brands-svg-icons';
	import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';
	import logo from '$lib/images/name.gif'; // Import the logo

	let isMenuOpen = false;

	function toggleMenu() {
		isMenuOpen = !isMenuOpen;
	}
</script>

<div class="nav-wrapper">
	<nav class="nav">
		<div class="nav-left">
			<div class="brand-logo"></div>
		</div>
		<div class="nav-center" class:is-open={isMenuOpen}>
			<a href="/" class="nav-button">Początek</a>
			<a href="/films" class="nav-button">Filmy</a>
			<a href="/faq" class="nav-button">FAQ</a>
			<a href="/contact" class="nav-button">Kontakt</a>
		</div>
		<div class="nav-right" class:is-open={isMenuOpen}>
			<a href="/discord" target="_blank" rel="noopener noreferrer">
				<FontAwesomeIcon icon={faDiscord} />
			</a>
			<a href="/youtube" target="_blank" rel="noopener noreferrer">
				<FontAwesomeIcon icon={faYoutube} />
			</a>
			<a href="/facebook" target="_blank" rel="noopener noreferrer">
				<FontAwesomeIcon icon={faFacebook} />
			</a>
			<a href="/tiktok" target="_blank" rel="noopener noreferrer">
				<FontAwesomeIcon icon={faTiktok} />
			</a>
		</div>
		<div class="menu-toggle">
			<button on:click={toggleMenu}>☰</button>
		</div>
	</nav>
</div>

<style>
	.nav-wrapper {
		border-bottom: 8px solid var(--theme-red);
		padding: 15px;
		backdrop-filter: blur(10px);
		background-color: rgba(0, 0, 0, 0.2);
	}

	.nav {
		height: 100px; /* Adjust the height as needed */
		max-width: 1424px;
		margin-left: auto;
		margin-right: auto;
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

	.brand-logo {
		height: 100px;
		width: 100%; /* Make the logo take up as much space as possible */

		background-image: url('$lib/images/name.gif');
		background-size: contain;
		background-repeat: no-repeat;
		background-position: fixed;
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
		font-size: 24px; /* Increased font size */
	}

	.nav-right a {
		color: inherit;
		font-size: 24px;
	}

	.menu-toggle {
		display: none;
	}

	@media (max-width: 768px) {
		.nav {
			flex-direction: column;
			align-items: center;
			gap: 25px;
		}

		.brand-logo {
			height: 100px;
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

		.nav-center.is-open,
		.nav-right.is-open {
			display: flex;
		}

		.menu-toggle {
			display: block;
		}
	}
</style>
