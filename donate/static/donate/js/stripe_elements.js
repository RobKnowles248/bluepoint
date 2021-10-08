/*
Logic, payment flow and styles from the stripe docs
https://stripe.com/docs/payments/accept-a-payment
*/
// Retrieve public and client secret keys
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

// Create an instance of Elements
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
    base: {
        color: '#000',
        fontFamily: '"Roboto", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '1rem',
    }
}

var card = elements.create('card', {style: style });
card.mount('#card-element');

// Error events
// card.on('change', ({error}) => {
//     let displayError = document.getElementById('#card-errors');
//     if (error) {
//         displayError.textContent = error.message;
//     } else {
//         displayError.textContent = '';
//     }
// });