package nvp;
import com.paypal.sdk.core.nvp.*;
import com.paypal.sdk.services.NVPCallerServices;

public class Checkout {

    public static void main(String[] args) {
        try {
            NVPCallerServices caller = new NVPCallerServices();
            NVPProfile profile = new NVPProfile();
            
            // Set up your API credentials and environment
            profile.setAPIUsername("YOUR_API_USERNAME");
            profile.setAPIPassword("YOUR_API_PASSWORD");
            profile.setSignature("YOUR_API_SIGNATURE");
            profile.setEnvironment("sandbox"); // Use "live" for production
            
            caller.setProfile(profile);
            
            // Create a new API request
            NVPDecoder decoder = new NVPDecoder();
            NVPEncoder encoder = new NVPEncoder();
            encoder.add("METHOD", "SetExpressCheckout");
            encoder.add("VERSION", "204"); // Specify the version of the API you're using
            encoder.add("PAYMENTREQUEST_0_AMT", "10.00"); // Set checkout amount
            encoder.add("PAYMENTREQUEST_0_CURRENCYCODE", "USD"); // Set currency
            encoder.add("RETURNURL", "http://yourwebsite.com/success"); // Set return URL after payment
            encoder.add("CANCELURL", "http://yourwebsite.com/cancel"); // Set cancel URL
            
            // Execute the API operation
            String strNVPRequest = encoder.encode();
            String strNVPResponse = caller.call(strNVPRequest);
            
            // Decode the response
            decoder.decode(strNVPResponse);
            
            if ("Success".equalsIgnoreCase(decoder.get("ACK"))) {
                System.out.println("Checkout initiated successfully.");
                // Extract token and redirect user for payment approval
                String token = decoder.get("TOKEN");
                // Redirect to PayPal for approval
                String redirectURL = "https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=" + token;
                System.out.println("Redirect user to: " + redirectURL);
            } else {
                System.out.println("Error: " + decoder.get("L_LONGMESSAGE0")); // Print error message
            }
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
