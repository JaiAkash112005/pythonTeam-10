import { render, screen } from '@testing-library/react';
import App from './App';

test('renders dashboard text', () => {
  render(<App />);
  const textElement = screen.getByText(/Campus Resource Management/i);
  expect(textElement).toBeInTheDocument();
});

