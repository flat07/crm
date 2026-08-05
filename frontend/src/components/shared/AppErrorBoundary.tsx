// frontend/src/components/shared/AppErrorBoundary.tsx

import { Component, type ErrorInfo, type ReactNode } from "react";

import ErrorState from "./ErrorState";

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
}

export default class AppErrorBoundary extends Component<Props, State> {
  state: State = {
    hasError: false,
  };

  static getDerivedStateFromError(): State {
    return {
      hasError: true,
    };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error(error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <ErrorState
          title="Application Error"
          description="Something unexpected happened."
        />
      );
    }

    return this.props.children;
  }
}
