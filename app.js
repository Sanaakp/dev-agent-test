"use strict";

/**
 * JavaScript entry point for browser or Node-based project logic.
 * Keep application behavior in functions so it can be tested independently.
 */

function createStatus(message = "Project is ready.") {
  let status = "ok";
  const normalizedMessage =
    typeof message === "string" && message.trim() ? message.trim() : "Project is ready.";

  return {
    status,
    message: normalizedMessage,
  };
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { createStatus };
}
