<!-- note: it is only meant for one container to be on the page -->
<div class="container"><slot /></div>

<style>
	.container {
		flex: 1 0 auto;
		max-width: var(--max-page-width);
		margin-inline: auto;
		padding-inline: 5vw;
		padding-top: 50px;
		padding-bottom: 50px;
	}
</style>
