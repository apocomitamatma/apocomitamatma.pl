<script>
	/** @type{{href: string, color?: string, noStyle?: boolean, children: import("svelte").Snippet}} */
	let { href, color, noStyle, children } = $props();
</script>

<a {href} style="color: {color}" data-no-style={noStyle} target="_blank" rel="noopener noreferrer">
	{@render children()}
</a>

<style>
	a[data-no-style='true'],
	a:hover[data-no-style='true'] {
		filter: none;
	}
</style>
