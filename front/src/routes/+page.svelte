<script>
	import { Carousel, FilmCounter, Logo } from '$lib/components';
	import { FiguresSprite } from '$lib/components/sprites';

	/** @type {Array<{category: 'e8' | 'mp' | 'mr', target: string}>} */
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
			<FiguresSprite />
			<div class="floating-statistics">
				<Carousel>
					<div class="landing-carousel-element">
						<div class="number-display">300+</div>
						<p>
							uczniów zadowolonych<br />
							z <a href="/contact">korepetycji</a><br />
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
		<div class="landing-item landing-right">
			<div class="landing-description">
				<Logo />
				<article>
					<i>Kolorowa matematyka z poczuciem humoru.</i><br /><br />
					Jesteś na stronie gdzie jest <a href="#o-mnie">trochę o mnie</a>,<br />
					<a href="/films">o moich filmach</a> i o
					<a href="/faq">pytaniach, które często dostaję</a>.<br /><br />
					<b>Szukasz korepetycji?</b> Zapraszam Cię
					<a href="/contact">tutaj</a>.<br />
				</article>
			</div>
		</div>
	</div>
</section>
<section id="o-mnie">
	<h1><a href="#o-mnie" class="section-name">O mnie</a></h1>
	<article>
		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse porta, dui porttitor
			tristique lacinia, metus mauris imperdiet risus, vel accumsan massa ex sed est. Donec auctor
			dignissim efficitur. Mauris lobortis consequat tellus, quis pharetra orci faucibus vitae.
			Phasellus auctor tempus rhoncus. Morbi lacinia gravida leo in consequat. Sed felis lectus,
			malesuada et tempus id, dictum id nulla. Nulla in erat sit amet quam tempor lacinia in et est.
		</p>
		<p>
			Nulla id tempus risus. Vestibulum ut maximus lorem, a finibus libero. Sed purus velit,
			facilisis eget ante vitae, sodales ultricies justo. Integer ante eros, sollicitudin quis nisi
			id, congue egestas lorem. Vestibulum laoreet enim vel ligula facilisis varius. Ut commodo
			lorem id tellus lacinia, id ultrices mi aliquam. Nullam sit amet magna ut risus condimentum
			volutpat. Nunc blandit tortor augue, ac efficitur est volutpat nec. Nulla laoreet in arcu a
			consequat. Nullam pretium, nulla non mollis venenatis, arcu nisi placerat mauris, et sodales
			nunc lacus non odio. Curabitur facilisis non ante non euismod. Vestibulum ante ipsum primis in
			faucibus orci luctus et ultrices posuere cubilia curae; Nunc lacinia, ante at auctor pretium,
			nisi est blandit mi, vitae vulputate urna tellus ut tellus.
		</p>
		<p>
			Vivamus hendrerit purus vitae egestas congue. Morbi euismod leo et vehicula tincidunt. Ut
			tincidunt magna at dui sagittis, ac luctus metus volutpat. Donec vitae elementum tellus, a
			iaculis magna. Curabitur ligula ipsum, interdum vel massa sit amet, tempor consectetur mauris.
			In finibus feugiat quam, nec dignissim nisl luctus nec. Suspendisse sapien mi, accumsan at
			lacinia vitae, varius vel urna. Donec venenatis elit ullamcorper augue porta convallis. Nunc
			in sodales risus. Aenean elementum, mi a malesuada dignissim, augue sapien dignissim sem, sed
			mollis orci mauris vitae urna. Proin non felis non metus porttitor ullamcorper nec nec erat.
			Aliquam erat volutpat. Phasellus porta libero justo, pulvinar tempus elit finibus at.
			Vestibulum ac ipsum vitae felis suscipit tincidunt volutpat eu mauris. Praesent gravida ex ut
			erat tempor, id mollis orci malesuada. Donec sodales sem et sapien feugiat, eget malesuada dui
			imperdiet.
		</p>
	</article>
</section>

<style>
	.landing {
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
		aspect-ratio: 1 / 1;
		position: relative;
	}

	.landing-right {
		flex: 1.5;
		text-align: center;
	}

	.number-display {
		font-weight: bold;
		font-size: 3em;
		margin-bottom: -20px;
		color: var(--theme-yellow);
	}

	.floating-statistics {
		filter: brightness(150%);
		position: absolute;
		bottom: 25%;
		height: 100px;
		margin-bottom: -20px;
		text-align: center;
		font-weight: bolder;
		font-size: 1.25em;
		text-shadow:
			10px 10px 10px #000000,
			10px 10px 10px #000000;
	}

	.floating-statistics a {
		color: var(--theme-yellow);
	}

	.floating-statistics a:hover {
		filter: brightness(80%);
	}

	.landing-carousel-element {
		display: flex;
		justify-content: center;
	}

	.landing-description {
		font-size: larger;
		text-wrap: balance;
		padding-top: 10px;
		padding-bottom: 10px;
	}

	@media (max-width: 1210px) {
		.landing {
			flex-direction: column;
		}
		:global(.logo) {
			margin-inlinet: auto;
		}

		.landing-left {
			max-height: 400px;
			justify-content: center;
		}
	}
</style>
