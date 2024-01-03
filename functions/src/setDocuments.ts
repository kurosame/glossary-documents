import * as logger from "firebase-functions/logger";
import { onRequest } from "firebase-functions/v2/https";

export const setDocuments = onRequest((_request, response) => {
  logger.info("Hello logs!", { structuredData: true });
  response.send("Hello from Firebase!");
});
