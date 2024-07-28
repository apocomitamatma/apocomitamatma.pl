<script>
	import { Carousel, FilmCounter, Logo, Sprite } from '$lib/components';

	import figuresSprite from '$lib/images/sprites/figures.png';

	const categories = [
		{ category: 'e8', target: 'ósmoklasistów' },
		{ category: 'mp', target: 'maturzystów<br>(poziom podstawowy)' },
		{ category: 'mr', target: 'maturzystów<br>(poziom rozszerzony)' }
	];
</script>

<svelte:head>
	<title>apocomitamatma.pl</title>
	<meta name="description" content="apocomitamatma.pl" />
</svelte:head>

<section>
	<div class="landing">
		<div class="landing-item landing-left landing-sprite">
			<Sprite imageUrl={figuresSprite} />
		</div>
		<div class="landing-item landing-right">
			<div class="landing-description">
				<Logo />
				<article>Kolorowa matematyka z poczuciem humoru.</article>
				<Carousel>
					<div class="landing-carousel-element">
						<div class="number-display">300+</div>
						<p>
							przeprowadzonych korepetycji<br />
							<a href="/contact">Kontakt...</a>
						</p>
					</div>
					{#each categories as { category, target }}
						<div class="landing-carousel-element">
							<div class="number-display"><FilmCounter {category} /></div>
							<p>filmów dla {@html target}</p>
						</div>
					{/each}
				</Carousel>
			</div>
		</div>
	</div>
</section>

<style>
	:global(.sprite-image) {
		/*
		I'm not really happy about these;
		They're image-dependent
		
		Perhaps adjust the images
		*/
		padding-left: 2%;
		padding-top: 7%;
	}

	a {
		color: var(--theme-blue);
		text-decoration: none;
	}

	a::hover {
		filter: brightness(120%);
	}

	.landing {
		margin-top: 5vh;
		margin-bottom: 5vh;
		display: flex;
		align-items: center;
		gap: 50px;
	}

	.landing-item {
		flex: 1;
		display: flex;
		justify-content: center;
	}

	.landing-left {
		flex: 1;
	}

	.landing-right {
		flex: 1.5;
	}

	.landing-description {
		font-size: xx-large;
	}

	.landing-carousel-element {
		display: flex;
		justify-content: center;
		min-height: 34vh;
		max-width: 600px;
	}

	.landing-carousel-element > p {
		margin-top: 150px;
	}

	.number-display {
		font-weight: bold;
		font-size: 4em;
		height: 100%;
		z-index: -1;
		margin-left: -5px;
		margin-top: -5px;
		color: var(--theme-blue);
		position: absolute;
	}

	@media (max-width: 1052px) {
		.landing {
			flex-direction: column;
		}
	}
</style>
