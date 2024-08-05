<script>
	let topic = $state(''); // Holds the "Piszę w sprawie" selection
	let educationLevel = $state('');
	let lessonType = $state('');
	let frequency = $state('');
	let cooperationType = $state('');
	let otherQuestions = $state('');
</script>

<svelte:head>
	<title>Kontakt | apocomitamatma.pl</title>
</svelte:head>

<section class="contact-form">
	<h1>Kontakt</h1>
	<form class="form-grid">
		<div class="form-left">
			<!-- Piszę w sprawie -->
			<div class="form-row">
				<fieldset>
					<legend>Interesują mnie...</legend>
					<label>
						<input type="radio" name="topic" value="korepetycje" bind:group={topic} />
						Korepetycje
					</label>
					<label>
						<input type="radio" name="topic" value="zapytania biznesowe" bind:group={topic} />
						Zapytania biznesowe
					</label>
					<label>
						<input type="radio" name="topic" value="inne" bind:group={topic} />
						Inne
					</label>
				</fieldset>
			</div>

			<!-- Display form fields based on the selection -->
			{#if topic === 'korepetycje'}
				<!-- Form for Korepetycje -->
				<div class="form-row">
					<fieldset>
						<legend>1. Poziom matematyki:</legend>
						<label>
							<input
								type="radio"
								name="educationLevel"
								value="Podstawowa"
								bind:group={educationLevel}
							/>
							Szkoła podstawowa, klasa…
						</label>
						<label>
							<input
								type="radio"
								name="educationLevel"
								value="Średnia (podstawowy)"
								bind:group={educationLevel}
							/>
							Szkoła średnia (poziom podstawowy), klasa…
						</label>
						<label>
							<input
								type="radio"
								name="educationLevel"
								value="Średnia (rozszerzony)"
								bind:group={educationLevel}
							/>
							Szkoła średnia (poziom rozszerzony), klasa…
						</label>
						<label>
							<input
								type="radio"
								name="educationLevel"
								value="Wyższa"
								bind:group={educationLevel}
							/>
							Szkoła wyższa, zakres…
						</label>
						<input type="text" placeholder="Zakres materiału" class="additional-input" />
					</fieldset>
				</div>

				<div class="form-row">
					<fieldset>
						<legend>2. Typ korepetycji który mnie interesuje:</legend>
						<label>
							<input type="radio" name="lessonType" value="Online" bind:group={lessonType} />
							Online
						</label>
						<label>
							<input type="radio" name="lessonType" value="Stacjonarnie" bind:group={lessonType} />
							Stacjonarnie
						</label>
						<label>
							<input type="radio" name="lessonType" value="Obojętne" bind:group={lessonType} />
							Obojętne
						</label>
					</fieldset>
				</div>

				<div class="form-row">
					<fieldset>
						<legend>3. Częstotliwość lekcji:</legend>
						<label>
							<input type="radio" name="frequency" value="Jednorazowo" bind:group={frequency} />
							Jednorazowo
						</label>
						<label>
							<input type="radio" name="frequency" value="Raz w tygodniu" bind:group={frequency} />
							Raz w tygodniu
						</label>
					</fieldset>
				</div>
			{:else if topic === 'zapytania biznesowe'}
				<!-- Form for Business Inquiries -->
				<div class="form-row">
					<fieldset>
						<legend>Rodzaj współpracy:</legend>
						<label>
							<input
								type="radio"
								name="cooperationType"
								value="Lokowanie produktu/usługi"
								bind:group={cooperationType}
							/>
							Lokowanie produktu/usługi na kanale „A po co Mi ta MATMA?”
						</label>
						<label>
							<input
								type="radio"
								name="cooperationType"
								value="Materiał edukacyjny"
								bind:group={cooperationType}
							/>
							Stworzenie przeze mnie materiału edukacyjnego na wyłączność
						</label>
						<label>
							<input
								type="radio"
								name="cooperationType"
								value="Inny"
								bind:group={cooperationType}
							/>
							Inny
						</label>
					</fieldset>
				</div>
			{/if}
			<button type="submit">Wyślij</button>
		</div>

		<div class="form-right">
			<!-- svelte-ignore a11y_label_has_associated_control -->
			<label>Piszę w sprawie:</label>
			<textarea bind:value={otherQuestions} placeholder="Opisz swoją sprawę..."></textarea>
		</div>
	</form>
</section>

<style>
	.contact-form {
		color: white;
		margin-bottom: var(--layout-padding-y);
	}

	.form-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 20px; /* Space between columns */
	}

	.form-left {
		grid-column: 1 / 2;
	}

	.form-right {
		grid-column: 2 / 3;
	}

	.form-full {
		grid-column: 1 / 3;
	}

	.form-row {
		margin-bottom: 20px; /* Space between form rows */
	}

	fieldset {
		border: 2px solid var(--theme-blue);
		border-radius: 5px;
	}

	legend {
		font-weight: bold;
		font-size: 1.2em;
		color: white;
	}

	textarea {
		width: 100%;
		height: 100%;
		min-height: 150px;
		font-size: 1.2em;
		padding: 10px;
		border-radius: 5px;
		border: 2px solid var(--theme-blue);
		background-color: rgba(255, 255, 255, 0.1);
		color: white;
	}

	label {
		display: block;
		margin-bottom: 10px;
		width: auto;
		text-align: left; /* Ensures text is aligned to the left */
	}

	.input-field label {
		width: 100%;
	}

	.input-field {
		width: 100%;
	}

	input[type='radio'] {
		margin-right: 10px;
	}

	.additional-input {
		width: 100%;
		margin-top: 10px;
		padding: 5px;
		border-radius: 5px;
		border: 2px solid var(--theme-blue);
		background-color: rgba(255, 255, 255, 0.1);
		color: white;
	}

	button {
		background-color: var(--theme-blue);
		color: white;
		padding: 10px 20px;
		font-size: 1.2em;
		border: none;
		border-radius: 5px;
		cursor: pointer;
		margin-top: 20px;
		width: 100%;
	}

	button:hover {
		background-color: var(--theme-yellow);
		color: black;
	}

	@media (max-width: 600px) {
		.form-grid {
			grid-template-columns: 1fr;
		}

		.form-left,
		.form-right,
		.form-full {
			grid-column: 1 / 2;
		}
	}
</style>
