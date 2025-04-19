export const login = async (username, password) => {
  try {
    console.log("[🟡 DEBUG] Sending login request...");
    console.log("[🟡 DEBUG] Username:", username);
    console.log("[🟡 DEBUG] Password:", password);

    const response = await fetch('/auth/login', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    console.log("[🟡 DEBUG] Response Status:", response.status);
    console.log("[🟡 DEBUG] Response Headers:", JSON.stringify([...response.headers]));

    const text = await response.text();
    console.log("[🟡 DEBUG] Raw response text:", text);

    if (!response.ok) {
      console.error("[❌ ERROR] Server returned non-OK:", response.status);
      throw new Error(text || 'Login failed');
    }

    const data = JSON.parse(text);
    console.log("[✅ DEBUG] Parsed response data:", data);
    return data.token;

  } catch (err) {
    console.error('[🔥 DEBUG] Final Caught Error:', err);
    throw err;
  }
};

