<!-- note: it is only meant for one container to be on the page -->
<div class="container"><slot /></div>

<style>
	.container {
		max-width: var(--max-page-width);
		margin-left: auto;
		margin-right: auto;
	}
</style>
