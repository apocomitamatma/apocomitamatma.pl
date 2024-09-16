<!-- note: it is only meant for one container to be on the page -->
<script>
	/** @type {{children: import("svelte").Snippet}} */
	let { children } = $props();
</script>

<div class="container">{@render children()}</div>

<style>
	.container {
		flex: 1 0 auto;
		width: 100vw;
		max-width: var(--layout-max-width);
		margin-inline: auto;
		padding-inline: var(--layout-padding-x);
		padding-top: var(--layout-padding-y);
		padding-bottom: var(--layout-padding-y);
	}
</style>
