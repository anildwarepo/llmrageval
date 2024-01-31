import com.paypal.base.rest.APIContext;
import com.paypal.base.rest.OAuthTokenCredential;
import com.paypal.base.rest.PayPalRESTException;

public class PayPalConfiguration {
    private static final String CLIENT_ID = "YOUR_CLIENT_ID";
    private static final String CLIENT_SECRET = "YOUR_CLIENT_SECRET";
    private static final String MODE = "sandbox"; // Use "live" for production

    public static APIContext getAPIContext() throws PayPalRESTException {
        // Get an access token from PayPal
        String accessToken = new OAuthTokenCredential(CLIENT_ID, CLIENT_SECRET)
                                 .getAccessToken();
        // Set up the APIContext with the access token
        return new APIContext(accessToken);
    }
}

import com.paypal.api.payments.*;
import com.paypal.base.rest.PayPalRESTException;

public class PayPalPaymentService {
    
    public Payment createPayment(Double total, String currency, 
                                 String method, String intent, 
                                 String description, String cancelUrl, 
                                 String successUrl) throws PayPalRESTException {
        // Set payment details
        Amount amount = new Amount();
        amount.setCurrency(currency);
        amount.setTotal(String.format("%.2f", total));

        Transaction transaction = new Transaction();
        transaction.setDescription(description);
        transaction.setAmount(amount);

        // Set the payer and payment method
        Payer payer = new Payer();
        payer.setPaymentMethod(method);

        // Create payment
        Payment payment = new Payment();
        payment.setIntent(intent);
        payment.setPayer(payer);
        payment.setTransactions(Arrays.asList(transaction));

        // Set redirect URLs
        RedirectUrls redirectUrls = new RedirectUrls();
        redirectUrls.setCancelUrl(cancelUrl);
        redirectUrls.setReturnUrl(successUrl);
        payment.setRedirectUrls(redirectUrls);

        // Execute API call
        APIContext apiContext = PayPalConfiguration.getAPIContext();
        return payment.create(apiContext);
    }
}
