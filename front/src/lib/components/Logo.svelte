<script>
	import logoImage from '$lib/images/brand.gif';

	let { inline = true } = $props();
</script>

<span class="logo">
	<img src={logoImage} data-inline={inline} alt="ApocoMItaMATMA.pl" />
</span>

<style>
	.logo img {
		max-width: var(--layout-logotype-width);
	}
	.logo img[data-inline='true'] {
		margin-bottom: -0.5em;
		max-height: 1.5em;
	}
</style>
