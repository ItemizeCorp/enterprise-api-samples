import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

import org.json.JSONObject;


public class ApiSampleCalls {

	private static final String API_URL =  "";
	private static final String DOCUMENTS_ENDPOINT =  "/documents";
	private static final String ACCOUNT_ID = "";
	private static final String API_TOKEN = "";

	private static String createBasicAuthHeader() {
		byte[] encodedAuth = Base64.getEncoder().encode(API_TOKEN.getBytes(StandardCharsets.UTF_8));
		return "Basic " + new String(encodedAuth);
	}

	/**
	 * Uploads a document to the Itemize API, 
	 * waits 60 seconds, 
	 * and then tries to retrieve the data for the uploaded document. 
	 * 
	 * If 200 is returned data is available and printed.
	 * If 404 is returned, document is still processing and data is not yet available.
	 * 
	 * @throws IOException
	 * @throws InterruptedException
	 */
	public static void main(String[] args) {
		try {
			String boundary = UUID.randomUUID().toString();

			Map<String, String> headers = new HashMap<>();

			headers.put("Authorization", createBasicAuthHeader());

			System.out.println("Trying to POST document...");
			ItemizeApiCall uploadCall = new ItemizeApiCall(
					API_URL + ACCOUNT_ID + DOCUMENTS_ENDPOINT, 
					headers,
					boundary);

			uploadCall.addFormField("metadata", "application/json", "{\"format\":\"image/jpeg\"}", boundary);
			uploadCall.addFilePart("document", new File("receipt.jpeg"), boundary);

			String response = uploadCall.finish(boundary);
			System.out.println(response);

			JSONObject jsonObj = new JSONObject(response);	    
			String guid = jsonObj.getString("id");

			System.out.println("Sleeping for 60 seconds...");
			Thread.sleep(60000);

			System.out.println("Trying to GET document: " + guid);
			ItemizeApiCall getCall = new ItemizeApiCall(
					API_URL + ACCOUNT_ID + DOCUMENTS_ENDPOINT + "/" + guid, 
					headers);	    

			response = getCall.getResponse();
			System.out.println(response);
		} catch(IOException | InterruptedException e) {
			e.printStackTrace();
		}
	}
}
