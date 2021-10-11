/*
Logic, payment flow and styles from the stripe docs
https://stripe.com/docs/payments/accept-a-payment
*/
// Retrieve public and client secret keys
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#client_secret').text().slice(1, -1);

// Create an instance of Elements
var stripe = Stripe(stripePublicKey);
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
let displayError = document.getElementById('#card-errors');
card.on('change', ({error}) => {
    if (error) {
        displayError.textContent = error.message;
    } else {
        displayError.textContent = '';
    }
});

// Submit payment to Stripe
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true)
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            displayError.textContent = result.error.message;
            card.update({'disabled': false});
            $('#submit-button').attr('disabled', false)
        } else {
            // displayError.textContent = '';
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});