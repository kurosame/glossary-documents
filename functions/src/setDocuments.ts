import logger from "firebase-functions/logger";
import { onObjectFinalized } from "firebase-functions/v2/storage";

export const setDocuments = onObjectFinalized({ timeoutSeconds: 540 }, (e) => {
  logger.info("Hello logs!", e.data.name);
});
