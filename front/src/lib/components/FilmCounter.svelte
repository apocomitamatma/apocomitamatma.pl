<script>
	import { onMount } from 'svelte';

	/**
	 * @type {string}
	 */
	export let category;

	let number = 0;
	let displayedNumber = '100';

	$: {
		let roundedNumber = Math.round(number / 10) * 10;
		displayedNumber = roundedNumber.toString() + (number % 10 == 0 ? '' : '+');
	}

	async function fetchStats() {
		try {
			const response = await fetch(`/api/stats/${category}`);
			const data = await response.json();

			if (!data['success']) {
				throw Error(`unsuccessful API response: ${data}`);
			}

			number = data['number'];
		} catch (error) {
			console.error('Error fetching stats:', error);
		}
	}

	onMount(fetchStats);
</script>

{displayedNumber}
