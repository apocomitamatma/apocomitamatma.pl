<div class="footer-wrapper">
	<footer class="footer">
		<div class="footer-row">
			<span class="footer-note footer-left">© 2024 apocomitamatma.pl</span>
			<span class="footer-note footer-right">
				Projekt i wykonanie strony: <a href="https://github.com/bswck">Bartosz Sławecki</a>
			</span>
		</div>
	</footer>
</div>

<style>
	:root {
		--footer-min-height: 100px;
	}

	.footer-wrapper {
		position: relative;
		bottom: 0;
		width: 100vw;
		border-top: 8px solid var(--theme-red);
		padding-top: 15px;
		padding-bottom: 15px;
		backdrop-filter: brightness(30%);
		background-color: rgba(0, 0, 0, 0.2);
	}

	.footer {
		min-height: var(--footer-min-height);
		max-width: var(--max-page-width);
		margin-left: auto;
		margin-right: auto;
		padding-left: 5vw;
		padding-right: 5vw;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.footer-row {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		width: 100%;
	}

	.footer-left {
		text-align: left;
	}

	.footer-right {
		text-align: right;
	}

	.footer-note {
		font-size: x-large;
	}

	@media (max-width: 1000px) {
		.footer-row {
			grid-template-columns: unset;
			gap: 1em;
		}

		.footer-right {
			text-align: left;
		}
	}
</style>
