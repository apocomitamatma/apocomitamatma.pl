<script>
	import { Logo } from '$lib/components';
	import { FiguresSprite } from '$lib/components/sprites';

	import FloatingStatistics from './FloatingStatistics.svelte';
</script>

<svelte:head>
	<title>apocomitamatma.pl</title>
	<meta name="description" content="apocomitamatma.pl" />
</svelte:head>

<section>
	<div class="landing">
		<div class="landing-item landing-left landing-sprite">
			<FiguresSprite />
			<FloatingStatistics />
		</div>
		<div class="landing-item landing-right">
			<div class="landing-description">
				<Logo />
				<article>
					<p><i>Kolorowa matematyka z poczuciem humoru.</i></p>
					<p>
						Jesteś na stronie gdzie jest <a href="#o-mnie">trochę o mnie</a>,
						<a href="/films">o moich filmach</a> <br />i o
						<a href="/faq">pytaniach, które często dostaję</a>.
					</p>
					<p>
						<b>Szukasz korepetycji?</b> Zapraszam Cię
						<a href="/contact">tutaj</a>.
					</p>
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
		/*
		I had an idea of making a flexbox that would only include the nav and landing
		but that conflicts heavily with the layout defined in +layout.svelte.

		As a trade-off, we're calculating the height of the landing to be 100vh
		in most browsers using this red-flag formula.
		*/
		height: calc(100vh - var(--layout-nav-min-height) - var(--layout-padding-y) - 35px);

		max-height: 900px;
		display: grid;
		justify-items: center;
		grid-template-columns: 1fr 1fr;
		align-items: center;
	}

	.landing-item {
		display: flex;
		justify-content: center;
	}

	.landing-left {
		aspect-ratio: 5 / 4;
		min-height: 300px;
		position: relative;
	}

	.landing-right {
		max-width: 30rem;
		overflow: visible;
		text-align: left;
	}

	.landing-description {
		font-size: var(--layout-emp-font-size);
		text-wrap: balance;
		padding-top: 10px;
		padding-bottom: 10px;
	}

	@media (max-width: 900px) {
		.landing {
			grid-template-columns: unset;
			gap: 20px;
			height: unset;
		}

		.landing-left {
			max-height: 400px;
			justify-content: center;
		}
	}
</style>
