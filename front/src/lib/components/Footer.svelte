<script>
	let year = $state(new Date().getFullYear());
</script>

<div class="footer-wrapper">
	<footer class="footer">
		<div class="footer-row">
			<span class="footer-note footer-left">© {year} apocomitamatma.pl</span>
			<span class="footer-note footer-right">
				Projekt i <a href="https://github.com/apocomitamatma/apocomitamatma.pl">wykonanie</a>
				strony:
				<a href="https://github.com/bswck" title="Lubię też matmę" style="white-space: nowrap">
					Bartosz Sławecki
				</a>
			</span>
		</div>
	</footer>
</div>

<style>
	.footer-wrapper {
		flex-shrink: 0;
		width: 100%;
		border-top: var(--layout-nav-border);
		padding-top: var(--layout-nav-padding-y);
		padding-bottom: var(--layout-nav-padding-y);
		backdrop-filter: brightness(30%);
		background-color: rgba(0, 0, 0, 0.2);
		z-index: 1;
	}

	.footer {
		min-height: var(--layout-nav-min-height);
		max-width: var(--layout-max-width);
		margin-inline: auto;
		padding-inline: var(--layout-padding-x);
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
		font-size: var(--layout-nav-font-size);
	}

	@media (max-width: 1030px) {
		.footer-row {
			padding-top: 20px;
			padding-bottom: 20px;
			grid-template-columns: unset;
			gap: 1em;
		}

		.footer-right {
			text-align: left;
		}
	}
</style>
