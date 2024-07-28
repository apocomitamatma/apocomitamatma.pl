<script>
	import Sprite from './Sprite.svelte';
	import Logo from './Logo.svelte';
	import figuresSprite from '$lib/images/sprites/figures.png';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="ApocoMItaMATMA.pl" />
</svelte:head>

<section>
	<div class="landing">
		<Sprite imageUrl={figuresSprite} />
		<Logo />
	</div>
</section>

<style>
	:global(.sprite-image) {
		padding-left: 2%;
		padding-top: 7%;
	}

	.landing {
		display: flex;
	}
</style>
