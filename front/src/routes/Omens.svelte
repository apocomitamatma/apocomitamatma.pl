<script>
	import { E8Omen, E8OmenAnimated } from '$lib/images/omens/';
	import { MPOmen, MPOmenAnimated } from '$lib/images/omens/';
	import { MROmen, MROmenAnimated } from '$lib/images/omens/';

	/** @type {Array<{omen: 'E8' | 'MP' | 'MR', srcStatic: string, srcAnimated: string}>} */
	const omens = [
		{ omen: 'E8', srcStatic: E8Omen, srcAnimated: E8OmenAnimated },
		{ omen: 'MP', srcStatic: MPOmen, srcAnimated: MPOmenAnimated },
		{ omen: 'MR', srcStatic: MROmen, srcAnimated: MROmenAnimated }
	];

	/**
	 * @param {MouseEvent & { currentTarget: EventTarget & HTMLAnchorElement }} event
	 * @param {string} src
	 */
	function changeChildImageSource(event, src) {
		const omen = event.currentTarget.querySelector('img');
		if (omen) {
			omen.src = src;
		}
	}
</script>

<div class="omens">
	{#each omens as { omen, srcStatic, srcAnimated }}
		<a
			href="/films/#{omen}"
			on:mouseenter={(event) => changeChildImageSource(event, srcAnimated)}
			on:mouseleave={(event) => changeChildImageSource(event, srcStatic)}
			data-omen={omen}
		>
			<img class="omen" src={srcStatic} alt={omen} />
		</a>
	{/each}
</div>

<style>
	.omens {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
	}
	.omen {
		width: 50%;
	}

	a::after {
		content: '';
		display: block;
		width: 0;
		height: var(--layout-nav-border-width);
		transition: width 0.4s ease-in;
	}

	a[data-omen='E8']::after {
		background-color: var(--theme-blue);
	}

	a[data-omen='MP']::after {
		background-color: var(--theme-yellow);
	}

	a[data-omen='MR']::after {
		background-color: var(--theme-red);
	}

	a:hover::after {
		width: 50%;
	}
</style>
