<!-- note: it is only meant for one container to be on the page -->
<div class="container"><slot /></div>

<style>
	.container {
		min-height: 100%;
		max-width: var(--max-page-width);
		margin-left: auto;
		margin-right: auto;
		padding-left: 5vw;
		padding-right: 5vw;
		padding-top: 5vh;
		padding-bottom: 5vh;
	}
</style>
