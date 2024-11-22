import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Alert, AlertDescription } from '@/components/ui/alert';

const EligibilityChecker = () => {
  const [studentId, setStudentId] = useState('');
  const [results, setResults] = useState(null);
  const [error, setError] = useState('');

  const checkEligibility = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/check-eligibility', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ student_id: studentId }),
      });

      if (!response.ok) {
        throw new Error('Failed to check eligibility');
      }

      const data = await response.json();
      setResults(data);
      setError('');
    } catch (err) {
      setError('Error checking eligibility. Please try again.');
      setResults(null);
    }
  };

  return (
    <Card className="w-full max-w-md mx-auto mt-8">
      <CardHeader>
        <CardTitle>Student Eligibility Checker</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          <div className="flex space-x-2">
            <Input
              type="text"
              placeholder="Enter Student ID"
              value={studentId}
              onChange={(e) => setStudentId(e.target.value)}
            />
            <Button onClick={checkEligibility}>Check</Button>
          </div>

          {error && (
            <Alert variant="destructive">
              <AlertDescription>{error}</AlertDescription>
            </Alert>
          )}

          {results && (
            <div className="space-y-2">
              <Alert>
                <AlertDescription>
                  <div className="font-medium">Results for Student ID: {results.student_id}</div>
                  <div className="mt-2">
                    <div>
                      Scholarship Eligible: 
                      <span className={results.scholarship_eligible ? 'text-green-600' : 'text-red-600'}>
                        {results.scholarship_eligible ? ' Yes' : ' No'}
                      </span>
                    </div>
                    <div>
                      Exam Permitted: 
                      <span className={results.exam_permitted ? 'text-green-600' : 'text-red-600'}>
                        {results.exam_permitted ? ' Yes' : ' No'}
                      </span>
                    </div>
                  </div>
                </AlertDescription>
              </Alert>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
};

export default EligibilityChecker;
