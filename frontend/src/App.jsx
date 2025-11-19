import React, { useEffect, useState } from "react";

export default function App() {
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);
  const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

  useEffect(() => {
    fetch(`${API}/api/reviews`)
      .then(res => res.json())
      .then(data => {
        setReviews(data);
      })
      .catch(err => {
        console.error("fetch error", err);
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <div style={{ fontFamily: "system-ui, Arial", padding: 20, maxWidth: 900, margin: "0 auto" }}>
      <h1>Product Reviews</h1>
      <p style={{ color: "#555" }}>Reviews collected over WhatsApp (twilio sandbox)</p>

      {loading ? (
        <div>Loading...</div>
      ) : (
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr style={{ textAlign: "left", borderBottom: "2px solid #ddd" }}>
              <th style={{ padding: "8px" }}>User</th>
              <th style={{ padding: "8px" }}>Product</th>
              <th style={{ padding: "8px" }}>Review</th>
              <th style={{ padding: "8px" }}>Time</th>
            </tr>
          </thead>
          <tbody>
            {reviews.length === 0 && (
              <tr><td colSpan="4" style={{ padding: 12 }}>No reviews yet</td></tr>
            )}
            {reviews.map(r => (
              <tr key={r.id} style={{ borderBottom: "1px solid #eee" }}>
                <td style={{ padding: 8 }}>{r.user_name ?? r.contact_number}</td>
                <td style={{ padding: 8 }}>{r.product_name}</td>
                <td style={{ padding: 8 }}>{r.product_review}</td>
                <td style={{ padding: 8 }}>{r.created_at ? new Date(r.created_at).toLocaleString() : "-"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
