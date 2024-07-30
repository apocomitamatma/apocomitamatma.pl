<script>
	import { Carousel, FilmCounter } from '$lib/components';

	/** @type {Array<{omen: 'E8' | 'MP' | 'MR', target: string}>} */
	const omens = [
		{ omen: 'E8', target: '<span style="color: var(--theme-blue)">ósmoklasistów</span>' },
		{
			omen: 'MP',
			target: 'maturzystów<br>(poziom <span style="color: var(--theme-yellow)">podstawowy</span>)'
		},
		{
			omen: 'MR',
			target: 'maturzystów<br>(poziom <span style="color: var(--theme-red)">rozszerzony</span>)'
		}
	];
</script>

<div class="floating-statistics">
	<Carousel>
		<div class="carousel-element">
			<div class="number-display">300+</div>
			<p>
				uczniów zadowolonych<br />
				z <a href="/contact">korepetycji</a><br />
			</p>
		</div>
		{#each omens as { omen, target }}
			<div class="carousel-element">
				<div class="number-display"><FilmCounter {omen} /></div>
				<p>filmów dla {@html target}</p>
			</div>
		{/each}
	</Carousel>
</div>

<style>
	.number-display {
		font-weight: bold;
		font-size: 3.5em;
		margin-bottom: -25px;
		color: var(--theme-yellow);
	}

	.floating-statistics {
		filter: brightness(150%);
		position: absolute;
		bottom: 20%;
		height: 100px;
		margin-bottom: -10%;
		text-align: center;
		font-weight: bolder;
		font-size: var(--layout-emp-font-size);
		/* Unfortunately, repeat() is only valid in grid-template-columns context */
		text-shadow:
			0px -1px 10px #000000,
			0px -1px 10px #000000,
			0px -1px 10px #000000;
	}

	.floating-statistics a {
		color: var(--theme-yellow);
	}

	.floating-statistics a:hover {
		filter: brightness(80%);
	}

	.carousel-element {
		display: flex;
		justify-content: center;
	}
</style>
