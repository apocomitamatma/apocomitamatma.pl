<script>
	import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';

	/** @type {{icon: any, animation?: any, size?: import('@fortawesome/fontawesome-svg-core').SizeProp}}*/
	let { icon, animation = 'bounce', size = 'xl' } = $props();
	let animate = $state.frozen(false);
</script>

<!-- svelte-ignore a11y_no_static_element_interactions -->
<span
	onmouseenter={() => {
		animate = true;
	}}
	onmouseleave={() => {
		animate = false;
	}}
>
	{#key animate}
		<FontAwesomeIcon {...{ [animation]: animate }} {icon} {size} />
	{/key}
</span>
