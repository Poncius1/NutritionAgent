function LayoutCentered({ children }) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-nutrition-sky via-nutrition-teal to-white flex items-center justify-center px-4">
      {children}
    </div>
  );
}

export default LayoutCentered;