'use client';

import { useEffect, useState, Suspense } from 'react';
import { useSearchParams, useRouter } from 'next/navigation';
import axios from 'axios';

const API_URL =  process.env.API_URL ||'http://localhost:8000';

function VerifyEmailContent() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const token = searchParams.get('token');
  const [status, setStatus] = useState('Verifying...');

  useEffect(() => {
    if (!token) {
      setStatus('Invalid token.');
      return;
    }

    axios.get(`${API_URL}/verify-email?token=${token}`)
      .then(() => {
        setStatus('Email verified successfully! Redirecting to login...');
        setTimeout(() => router.push('/login'), 3000);
      })
      .catch((err) => {
        setStatus(err.response?.data?.detail || 'Verification failed.');
      });
  }, [token, router]);

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="p-8 bg-white rounded-lg shadow-lg">
        <h2 className="text-xl font-bold mb-4">Email Verification</h2>
        <p>{status}</p>
      </div>
    </div>
  );
}

export default function VerifyEmail() {
  return (
    <Suspense fallback={
      <div className="flex justify-center items-center h-screen bg-background">
        <div className="w-10 h-10 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
      </div>
    }>
      <VerifyEmailContent />
    </Suspense>
  );
}
