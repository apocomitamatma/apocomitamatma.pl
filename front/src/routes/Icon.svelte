<script>
	import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';

	export let icon;
	let bounce = false;

	function enter() {
		bounce = true;
	}

	function leave() {
		bounce = false;
	}
</script>

<!-- svelte-ignore a11y_no_static_element_interactions -->
<div on:mouseenter={enter} on:mouseleave={leave}>
	{#key bounce}
		<FontAwesomeIcon {bounce} {icon} />
	{/key}
</div>
