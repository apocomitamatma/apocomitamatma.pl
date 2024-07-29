<script>
	import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';

	export let icon;

	/** @type {import('@fortawesome/fontawesome-svg-core').SizeProp}*/
	export let size = 'xl';
	let bounce = false;
</script>

<!-- svelte-ignore a11y_no_static_element_interactions -->
<div
	on:mouseenter={() => {
		bounce = true;
	}}
	on:mouseleave={() => {
		bounce = false;
	}}
>
	{#key bounce}
		<FontAwesomeIcon {bounce} {icon} {size} />
	{/key}
</div>
