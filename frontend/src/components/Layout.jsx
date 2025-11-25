function Layout({ children }) {
  return (
    <div className="min-h-screen flex items-center justify-center px-4 py-8">
      <div className="w-full max-w-5xl">
        {children}
      </div>
    </div>
  );
}

export default Layout;